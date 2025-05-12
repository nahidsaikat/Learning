from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.article.models import Article
from app.user.models import User
from app.article.schemas import ArticleCreate, ArticleResponse, ArticleUpdate
from app.dependencies import get_db
from app.utils.auth import get_current_active_user

article_router = APIRouter(tags=["articles"])


@article_router.post("/articles", response_model=ArticleResponse)
def create_article(
    article: ArticleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_article = Article(
        **article.model_dump(),
        author_id=current_user.id
    )
    
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    
    return db_article


@article_router.get("/articles", response_model=List[ArticleResponse])
def read_articles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # If user is admin, show all published articles, otherwise only user's articles
    if current_user.is_admin:
        articles = db.query(Article).filter(Article.published == True).offset(skip).limit(limit).all()
    else:
        articles = db.query(Article).filter(
            (Article.author_id == current_user.id) | (Article.published == True)
        ).offset(skip).limit(limit).all()
    
    return articles


@article_router.get("/articles/{article_id}", response_model=ArticleResponse)
def read_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    
    if article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    # Only the author or admins can see unpublished articles
    if not article.published and article.author_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this article"
        )
    
    return article


@article_router.put("/articles/{article_id}", response_model=ArticleResponse)
def update_article(
    article_id: int,
    article_update: ArticleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    # Only the author or admins can update articles
    if db_article.author_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this article"
        )
    
    # Update article with non-None values
    update_data = article_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_article, key, value)
    
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    
    return db_article


@article_router.delete("/articles/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found"
        )
    
    # Only the author or admins can delete articles
    if db_article.author_id != current_user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this article"
        )
    
    db.delete(db_article)
    db.commit()
    
    return None
