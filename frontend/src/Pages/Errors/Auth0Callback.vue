<script setup>
import {useAuth0} from "@auth0/auth0-vue";

const {error} = useAuth0()
</script>
<template>
  <div v-if="error" class="min-h-screen w-screen flex flex-col gap-10 justify-center items-center bg-gray-900">
    <h1 class="text-2xl font-extralight uppercase text-gray-500">Error</h1>
    <p class="bg-gray-100 dark:bg-gray-800 rounded-md p-2 text-xs font-mono text-left">{{ error }}</p>
  </div>
</template>