import React, { useState, useEffect, Fragment } from 'react';
import { Helmet } from 'react-helmet';
import axios from 'axios';
import House from '../assets/images/house.jpg';

const About = () => {
    const [topSeller, setTopSeller] = useState([]);
    const [realtors, setRealtors] = useState([]);

    useEffect(() => {
        axios.defaults.headers = {
            'Content-Type': 'application/json'
        };

        const getTopSeller = async () => {
            try {
                const res = await axios.get('http://localhost:8000/api/realtors/topseller/');
                setTopSeller(res.data);
            }
            catch (err) {

            }
        };

        getTopSeller();
    }, []);

    useEffect(() => {
        axios.defaults.headers = {
            'Content-Type': 'application/json'
        };

        const getRealtors = async () => {
            try {
                const res = await axios.get('http://localhost:8000/api/realtors/');
                setRealtors(res.data);
            }
            catch (err) {

            }
        };

        getRealtors();
    }, []);

    const getAllRealtors = () => {
        let allRealtors = [];
        let results = [];

        realtors.map(realtor => {
            return allRealtors.push(
                <Fragment key={realtor.id}>
                    <div className='about__display'>
                        <img className='about__display__image' src={realtor.photo} alt='' />
                    </div>

                    <h3 className='about__realtor'>{realtor.name}</h3>
                    <p className='about__contact'>{realtor.phone}</p>
                    <p className='about__contact'>{realtor.email}</p>
                    <p className='about__about'>{realtor.description}</p>
                </Fragment>
            );
        });

        for (let i=0; i<realtors.length; i+=3) {
            results.push(
                <div key={i} className='row'>
                    <div className='col-1-of-3'>
                        {allRealtors[i]}
                    </div>
                    <div className='col-1-of-3'>
                        {allRealtors[i+1] ? allRealtors[i+1] : null}
                    </div>
                    <div className='col-1-of-3'>
                        {allRealtors[i+2] ? allRealtors[i+2] : null}
                    </div>
                </div>
            );
        }

        return results;
    };

    const getTopSeller = () => {
        let result = [];

        topSeller.map(seller => {
            return result.push(
                <Fragment key={seller.id}>
                    <div className='about__display'>
                        <img className='about__display__image' src={seller.photo} alt='' />
                    </div>
                    <h3 className='about__topseller'>Top Seller</h3>
                    <p className='about__realtor'>{seller.name}</p>
                    <p className='about__contact'>{seller.phone}</p>
                    <p className='about__contact'>{seller.email}</p>
                    <p className='about__about'>{seller.description}</p>
                </Fragment>
            );
        });

        return result;
    };

    return (
        <main className='about'>
            <Helmet>
                <title>Realest Estate - About</title>
                <meta 
                    name='description'
                    content='About Us'
                />
            </Helmet>
            <header className='about__header'>
                <h1 className='about__heading'>About Realest Estate</h1>
            </header>
            <section className='about__info'>
                <div className='row'>
                    <div className='col-3-of-4'>
                        <h2 className='about__subheading'>We find the perfect home for you</h2>
                        <p className='about__paragraph'>
                            Cras posuere dictum mattis. Proin malesuada at lacus ut tincidunt. 
                            Interdum et malesuada fames ac ante ipsum primis in faucibus. 
                            Cras feugiat, quam eget pharetra porttitor, arcu nulla aliquet 
                            risus, eget congue mauris sem vitae enim. Integer eget nunc nec 
                            arcu molestie commodo. Duis rhoncus mollis euismod. 
                            Phasellus congue at ante non imperdiet. Suspendisse congue nibh 
                            at mi mollis fermentum.
                        </p>
                        <div className='about__display'>
                            <img className='about__display__image' src={House} alt='' />
                        </div>
                        <p className='about__paragraph'>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                            Praesent non nulla eleifend, pulvinar quam eget, rutrum quam. 
                            Sed nec risus nec arcu eleifend pretium. Curabitur in dui odio. 
                            Vivamus mollis magna in nulla laoreet, nec volutpat metus efficitur. 
                            Nam viverra euismod ante gravida sodales. Ut imperdiet magna ut lobortis consequat. 
                            Curabitur scelerisque ac risus ac imperdiet. Donec mollis rutrum eros quis porta. 
                            Nullam ac egestas dui, at eleifend enim. Donec et turpis viverra, sodales orci eu,
                            sodales eros. In scelerisque, odio in malesuada posuere, quam quam aliquam nunc, 
                            a aliquam enim neque non metus. Sed in varius ante. 
                        </p>
                    </div>
                    <div className='col-1-of-4'>
                        {getTopSeller()}
                    </div>
                </div>
            </section>
            <section className='about__team'>
                <div className='row'>
                    <h2 className='about__subheading'>Meet your awesome team</h2>
                </div>
                {getAllRealtors()}
            </section>
        </main>
    );
};

export default About;
