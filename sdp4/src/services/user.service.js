import axios from 'axios';

const API_URL = 'http://localhost:8000/';

const getDoctors = () => axios.get(`${API_URL}doctors`);
const getDoctor = id => axios.get(`${API_URL}doctors/${id}`);
const getAppointments = id => axios.get(`${API_URL}appointments/${id}`);
const getAppointment = appointmentId => axios.get(`${API_URL}appointment/${appointmentId}`);
const postAppointment = (userId, doctorId, appointmentDate) => axios.post(`${API_URL}add/appointment`, { doctor_id: doctorId, appointment_date: appointmentDate, user_id: userId });
const deleteAppointment = appointmentId => axios.delete(`${API_URL}delete/${appointmentId}`);
export default {
  getDoctors,
  getDoctor,
  getAppointments,
  getAppointment,
  postAppointment,
  deleteAppointment,
};
