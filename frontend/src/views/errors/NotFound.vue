<template>
    <div class="not-found">
        <h1>404 - Página No Encontrada</h1>
        <p>Lo sentimos, no pudimos encontrar la página que buscas.</p>
        <router-link to="/">Volver a la página de inicio</router-link>
    </div>
</template>

<script>
export default {
name: 'NotFound',
};
</script>

<style scoped>
.not-found {
text-align: center;
margin-top: 50px;
}

.not-found h1 {
font-size: 3em;
color: #f44336;
}

.not-found p {
font-size: 1.2em;
}

.not-found a {
color: #42b983;
text-decoration: none;
font-weight: bold;
}
</style>
