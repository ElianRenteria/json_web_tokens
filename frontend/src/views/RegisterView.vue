<template>
  <div class="container">
    <div class="card">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Username" required>
        <input type="password" v-model="password" placeholder="Password" required>
        <button type="submit">Register</button>
      </form>
      <button class="link-button" @click="goToLogin">Login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:5000/register', {
          username: this.username,
          password: this.password
        });
        console.log('Register successful:', response.data); // Log the response data
        this.$router.push('/');
      } catch (error) {
        console.error('Register error:', error.response ? error.response.data : error.message); // Log detailed error info
      }
    },
    goToLogin() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.card {
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background-color: white;
  text-align: center;
}

input {
  display: block;
  margin: 0.5rem 0;
  padding: 0.5rem;
  width: 100%;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.link-button {
  margin-top: 1rem;
  background: none;
  color: #007bff;
  cursor: pointer;
}

.link-button:hover {
  text-decoration: underline;
}
</style>
