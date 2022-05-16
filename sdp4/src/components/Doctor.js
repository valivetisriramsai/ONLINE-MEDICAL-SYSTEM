import React, { useState, useEffect } from 'react';
import { Redirect, Link, useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import UserService from '../services/user.service';
import classes from '../styles/Doctor.module.css';

const Doctor = () => {
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(true);
  const { user: currentUser } = useSelector(state => state.auth);

  if (!currentUser) {
    return <Redirect to="/login" />;
  }
  const { id } = useParams();
  useEffect(() => {
    UserService.getDoctor(id).then(
      response => {
        setLoading(false);
        setContent(response.data);
      },
      error => {
        setLoading(false);
        const message = (error.response
            && error.response.data
            && error.response.data.message)
          || error.message
          || error.toString();

        setContent(message);
      },
    );
  }, []);
  return (
    <div className="container">
      <div className="text-center">
        {loading && <span className="spinner-border spinner-border-lg" />}
      </div>
      <div className={classes.Doctor}>
        <img src="data:image/jpeg;base64,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" alt={content.name} className={classes.doctorImg} />
        <div>
          <h2>
            {content.name}
          </h2>
          <p className={`${classes.badge} ${classes.badgeSecondary}`}>
            Appointment Fee &nbsp;&nbsp;&nbsp;&nbsp; Rs. 300
          </p>
          <p className={classes.badge}>
            Qualification: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {content.Qualification}
          </p>
          <p className={`${classes.badge} ${classes.badgeSecondary}`}>
            Experience: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {content.Experience}
            &nbsp;  Years
          </p>
          <p className={classes.badge}>
            Department: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Medicine
          </p>
          <li>
            <Link
              to={{
                pathname: '/appointments/new',
                doctorId: content.id,
              }}
              className={classes.btn}
            >
              Add Appointment
            </Link>
          </li>
        </div>
      </div>
    </div>
  );
};

export default Doctor;
