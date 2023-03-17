<script setup>
import {useAuth0} from "@auth0/auth0-vue";

const {logout} = useAuth0();

const handleLogout = () =>
    logout({
      logoutParams: {
        returnTo: `${window.location.origin}/login`,
      }
    });
</script>
<template>
  <button
      type="button"
      @click="handleLogout"
  >
    <slot />
  </button>
</template>
