<script setup>
import moment from "moment";
const year_now = moment().year()
</script>
<template>
<div class="min-h-screen w-screen flex flex-col justify-between items-center bg-gray-50 dark:bg-gray-900">
  <div></div>
  <slot/>
  <div class="text-center text-xs"><span v-text="year_now"></span> &copy; D.I.C.E. Systems. All Rights Reserved</div>
</div>
</template>

