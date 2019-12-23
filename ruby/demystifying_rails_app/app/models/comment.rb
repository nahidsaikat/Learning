class Comment
    attr_reader :id, :body, :author, :post_id, :created_at
  
    def initialize(attributes={})
      @id = attributes['id'] if new_record?
      @body = attributes['body']
      @author = attributes['author']
      @post_id = attributes['post_id']
      @created_at ||= attributes['created_at']
    end
  
    def new_record?
      @id.nil?
    end
end
