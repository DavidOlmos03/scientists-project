<script setup>
  import { RouterView } from 'vue-router';
  import NavBar from '@/components/NavBar.vue';
  import Footer from '@/components/Footer.vue';

</script>


<template>
  <div id="app" class="p-4 px-6 lg:px-8">
    <header>
      <NavBar />
      <!-- <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/contact">Contact</router-link></li>
        </ul>
      </nav> -->
    </header>

    <!-- View rendered based on the route -->
    <RouterView />

    <!-- Footer -->
     <div>
       <Footer />
     </div>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<!-- <style>

body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #42b983;
  padding: 1em;
  color: white;
  min-width: 100%;
  min-height: 100%;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 1em;
}

footer {
  text-align: center;
  padding: 1em;
  background-color: #f1f1f1;
  position: fixed;
  width: 100%;
  bottom: 0;
}
</style> -->

