<script setup>
import AuthLayout from '@/Layouts/AuthLayout.vue'
</script>


<template>
  <AuthLayout>
    <div
        class="bg-white shadow-md border border-gray-200 rounded-lg max-w-sm p-4 sm:p-6 lg:p-8 dark:bg-gray-800 dark:border-gray-700">
      <section>
        <slot/>
      </section>
      <footer class="flex justify-end p-5">
        <slot name="footer"/>
      </footer>
    </div>
  </AuthLayout>
</template>