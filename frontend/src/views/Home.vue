<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      msg:""
    };
  },
  methods: {
    getResponse() {
      const path = 'http://127.0.0.1:5000/';
      axios.get(path)
      .then(res => {
        console.log(res.data);
        this.msg = res.data;
      }).catch(err => {
        console.log(err);
      });
    }
  }, 
  created() {
    this.getResponse();
  }
}

</script>

<template>
  <div>
    <h1>Welcome to the Home Page</h1>
    <p>{{ msg }}</p>
  </div>
</template>

<style>
h1 {
  color: #42b983;
}
</style>
