
<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Card from '@/components/Card.vue';
import { RouterView } from 'vue-router';

const library = ref("");

const getResponse = async () => {
  const path = 'http://127.0.0.1:5000/library';
  try {
    const res = await axios.get(path);
    console.log(res.data);
    library.value = res.data; 
  } catch (err) {
    console.error(err);
  }
};

onMounted(() => {
  getResponse();
});

</script>

<template>
	<h1>
		This is a full library 
	</h1>
	<p>{{library}}</p>

	<div class="pt-32 container mx-auto lg-min-h-screen">
            <RouterView />
        </div>
</template>
