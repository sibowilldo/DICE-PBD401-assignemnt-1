<script setup>
import {useAuth0} from "@auth0/auth0-vue";

const {loginWithRedirect} = useAuth0();

const handleLogin = () => loginWithRedirect();


</script>
<template>
  <button type="button" @click="handleLogin">
    <slot/>
  </button>
</template>
