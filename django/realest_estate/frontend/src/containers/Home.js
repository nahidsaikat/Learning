import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import { setAlert } from '../actions/alert';
import ListingForm from '../components/ListingForm';
import Listings from '../components/Listings';
import Pagination from '../components/Pagination';;

const Home = () => {
    const [listings, setListings] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [listingsPerPage, setListingsPerPage] = useState(3);
    const [active, setActive] = useState(1);

    const indexOfLastListing = currentPage * listingsPerPage;
    const indexOfFirstListing = indexOfLastListing - listingsPerPage;
    const currentListings = listings.slice(indexOfFirstListing, indexOfLastListing);

    const visitPage = (page) => {
        setCurrentPage(page);
        setActive(page);
    };

    const previousNumber = () => {
        if (currentPage !== 1) {
            setCurrentPage(currentPage-1);
            setActive(currentPage-1);
        }
    };

    const nextNumber = () => {
        if (currentPage !== Math.ceil(listings.length/3)) {
            setCurrentPage(currentPage+1);
            setActive(currentPage+1);
        }
    };

    return (
        <main className='home'>
            <Helmet>
                <tilte>Realest Estate - Home</tilte>
                <meta 
                    name='description'
                    content='Realest Estate Home Page'
                />
            </Helmet>
            <section className='home__form'>
                <ListingForm setListings={setListings} />
            </section>
            <section className='home__listings'>
                <Listings listings={currentListings} />
            </section>
            <section className='home__pagination'>
                <div className='row'>
                    {
                        listings.length !== 0 ? (
                            <Pagination
                                itemsPerPage={listingsPerPage}
                                count={listings.length}
                                visitPage={visitPage}
                                previous={previousNumber}
                                next={nextNumber}
                                active={active}
                                setActive={setActive}
                            />
                        ) : null
                    }
                </div>
            </section>
        </main>
    );
};

export default Home;
