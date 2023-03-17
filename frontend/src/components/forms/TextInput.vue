<script setup>
import {computed} from "vue";

const props = defineProps({
  modelValue:String,
  type: String
})
const emit = defineEmits(['update:modelValue'])
const value = computed({
  get() {
    return props.modelValue
  },
  set(value) {
    emit('update:modelValue', value)
  }
})
</script>

<template>
  <input
      class="mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1
                           dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                           ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset
                           focus:ring-indigo-600 sm:text-sm sm:leading-6"
      :type="type"
      v-model="value"
  />
</template>