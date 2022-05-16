import axios from 'axios';

const API_URL = 'http://localhost:8000/';

const register = (name, email, password) => axios.post(`${API_URL}add`, {
  name,
  email,
  password,
})
  .then(response => {
    if (response.data.jwt) {
      localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response;
  });

const login = (email, password) => axios
  .post(`${API_URL}login_auth`, {
    email,
    password,
  })
  .then(response => {
    localStorage.setItem('user', JSON.stringify(response.data));
    return response.data;
  });

const logout = () => {
  localStorage.removeItem('user');
};

export default {
  register,
  login,
  logout,
};
