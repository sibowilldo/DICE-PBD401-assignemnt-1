<script setup>
import {useAuth0} from "@auth0/auth0-vue";
import Loading from "@/components/Loading.vue";
import AsideDrawer from "@/Layouts/AsideDrawer.vue";
import TopNavigationBar from "@/Layouts/TopNavigationBar.vue";

const {isLoading} = useAuth0()
</script>
<template>
  <Loading v-if="isLoading" class="min-h-screen w-full flex flex-col gap-5 justify-center items-center"/>
  <div class="min-h-screen w-screen">
    <!-- ------ TopNavigationBar ------- -->
    <TopNavigationBar/>
    <!-- ------ ASIDE ------- -->
    <AsideDrawer/>
    <div class="p-4 sm:ml-64 flex flex-col items-stretch">
      <div class="mt-14 ml-8 text-3xl font-extralight">
        <slot name="page_header"></slot>
      </div>
      <div class="p-4 mt-8 max-w-6xl">
        <slot/>
      </div>
    </div>
  </div>
</template>




