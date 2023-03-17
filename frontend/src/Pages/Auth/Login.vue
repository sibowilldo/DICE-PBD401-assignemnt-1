<script setup>
import {useAuth0} from "@auth0/auth0-vue";
import AuthCard from "@/Layouts/AuthCard.vue";
import Logo from "@/components/common/Logo.vue";
import LoginButton from "@/components/common/LoginButton.vue";
import LogoutButton from "@/components/common/LogoutButton.vue";
import {ArrowLeftOnRectangleIcon} from "@heroicons/vue/20/solid";

// declarations & initializations
const {isAuthenticated} = useAuth0();

</script>

<template>
  <AuthCard>
    <div class="flex justify-center flex-col align-middle items-center p-5 min-h-60 text-center">
      <router-link to="/">
        <Logo :class="'w-[150px] mb-5 flex justify-center  items-center'"/>
      </router-link>
      <h1 class="text-2xl font-bold">Welcome Back!</h1>
      <p class="text-gray-400 text-sm ">Sign in to your account to get started</p>
    </div>
    <template #footer>
      <div class="flex flex-col items-center gap-5 justify-between w-full">
        <LoginButton v-if="!isAuthenticated" :class="'flex bg-blue-400 px-4 py-2 rounded-md hover:bg-blue-500'">
          <svg aria-hidden="true"
               class="flex-shrink-0 w-6 h-6 text-white transition duration-75 dark:text-white group-hover:text-gray-900 dark:group-hover:text-white"
               fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd"
                  d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z"
                  fill-rule="evenodd"></path>
          </svg>
          <span class="flex-1 ml-3 whitespace-nowrap">Sign In</span>
        </LoginButton>
        <LogoutButton v-else :class="'bg-red-700 hover:bg-red-400 dark:bg-red-700 py-2 px-4 rounded flex align-middle gap-2'">
          <ArrowLeftOnRectangleIcon class="text-gray-200 h-5 w-5"/>
          Sign Out
        </LogoutButton>
        <span class="text-xs">Powered by Auth0</span>
      </div>
    </template>
  </AuthCard>
</template>
