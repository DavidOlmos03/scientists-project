<template>
    <div class="error">
        <h1>Error 500 - Problema en el Servidor</h1>
        <p>Lo sentimos, algo salió mal. Por favor intenta más tarde.</p>
        <router-link to="/">Volver a la página de inicio</router-link>
    </div>
</template>

<script>
export default {
name: 'Error',
};
</script>

<style scoped>
.error {
text-align: center;
margin-top: 50px;
}

.error h1 {
font-size: 3em;
color: #f44336;
}

.error p {
font-size: 1.2em;
}

.error a {
color: #42b983;
text-decoration: none;
font-weight: bold;
}
</style>