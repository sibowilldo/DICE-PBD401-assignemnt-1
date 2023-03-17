
<script setup>
import Logo from "@/components/common/Logo.vue";
import LogoutButton from "@/components/common/LogoutButton.vue";
import {ref} from "vue";

const sidebarOpen = ref(false)
</script>
<template>
  <nav class="fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
    <div class="px-3 py-3 lg:px-5 lg:pl-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center justify-start">
          <button aria-controls="logo-sidebar"
                  class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                  data-drawer-target="logo-sidebar"
                  @click="!sidebarOpen"
                  type="button">
            <span class="sr-only">Open sidebar</span>
            <svg aria-hidden="true" class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path clip-rule="evenodd"
                    d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
                    fill-rule="evenodd"></path>
            </svg>
          </button>
          <router-link class="flex ml-2 md:mr-24" to="/">
            <Logo :class="'w-[100px] flex justify-center  items-center'"/>
          </router-link>
        </div>
        <div class="flex items-center">
          <div class="flex items-center ml-3 relative">
            <div>
              <button aria-expanded="false"
                      class="flex text-sm bg-gray-800 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600"
                      data-dropdown-toggle="dropdown-user" type="button">
                <span class="sr-only">Open user menu</span>
                <img alt="user photo" class="w-8 h-8 rounded-full"
                     src="https://flowbite.com/docs/images/people/profile-picture-5.jpg">
              </button>
            </div>
            <div
                id="dropdown-user"
                class="hidden absolute right-0 top-6 z-50 my-4 text-base list-none bg-white divide-y divide-gray-100 rounded shadow dark:bg-gray-700 dark:divide-gray-600">
              <div class="px-4 py-3" role="none">
                <p class="text-sm text-gray-900 dark:text-white" role="none">
                  Neil Sims
                </p>
                <p class="text-sm font-medium text-gray-900 truncate dark:text-gray-300" role="none">
                  neil.sims@flowbite.com
                </p>
              </div>
              <ul class="py-1" role="none">
                <li>
                  <a class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                     href="#"
                     role="menuitem">Dashboard</a>
                </li>
                <li>
                  <a class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                     href="#"
                     role="menuitem">Settings</a>
                </li>
                <li>
                  <LogoutButton
                      :class="'block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white'"
                      role="menuitem">Earnings
                  </LogoutButton>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>