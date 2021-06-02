import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './containers/Home';
import About from './containers/About';
import Contact from './containers/Contact';
import Listing from './containers/Listings';
import ListingDetail from './containers/ListingDetail';
import LogIn from './containers/LogIn';
import SignUp from './containers/SignUp';
import NotFound from './components/NotFound';
import Layout from './hocs/Layout';

import './sass/main.scss';

const App = () => (
  <Router>
    <Layout>
      <Switch>
        <Route exact path='/' component={Home} />
        <Route exact path='/about' component={About} />
        <Route exact path='/contact' component={Contact} />
        <Route exact path='/listing' component={Listing} />
        <Route exact path='/listing/:id' component={ListingDetail} />
        <Route exact path='/login' component={LogIn} />
        <Route exact path='/signup' component={SignUp} />
        <Route component={NotFound} />
      </Switch>
    </Layout>
  </Router>
);

export default App;