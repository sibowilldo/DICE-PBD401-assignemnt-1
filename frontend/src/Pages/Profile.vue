<script setup>
import AppLayout from '@/Layouts/AppLayout.vue'
import {useAuth0} from '@auth0/auth0-vue'

// declarations & initializations
const {user} = useAuth0();
</script>
<template>
  <AppLayout>
    <div>
      <h2>Profile</h2>

      <pre class="bg-gray-100 dark:bg-gray-800 rounded-md p-2 text-xs font-mono text-left">
                <code>{{ user ? JSON.stringify(user.value, null, 2) : "Nothing" }}</code>
            </pre>
    </div>
  </AppLayout>
</template>