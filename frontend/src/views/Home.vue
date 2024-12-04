<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Card from '@/components/Card.vue';

const msg = ref("");

const getResponse = async () => {
  const path = 'http://127.0.0.1:5000/';
  try {
    const res = await axios.get(path);
    console.log(res.data);
    msg.value = res.data; 
  } catch (err) {
    console.error(err);
  }
};

onMounted(() => {
  getResponse();
});

</script>

<template>
  <div>
    <h1>Welcome to the Home Page</h1>

    <p>{{ msg }}</p>

    <Card />
    <Card />
    <Card />
  </div>
</template>


