<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 font-sans antialiased transition-colors duration-300">
    <Login v-if="!isLoggedIn" @login-success="checkLogin" />
    <Dashboard v-else @logout="handleLogout" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Login from './components/Login.vue';
import Dashboard from './components/Dashboard.vue';

const isLoggedIn = ref(false);

const checkLogin = () => {
  const token = localStorage.getItem('token');
  isLoggedIn.value = !!token;
};

const handleLogout = () => {
  localStorage.removeItem('token');
  isLoggedIn.value = false;
};

onMounted(() => {
  checkLogin();
  
  // Initialize theme (default to light for this design based on images, or respect system)
  // The design images are light mode, so we'll ensure good defaults.
  if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
});
</script>