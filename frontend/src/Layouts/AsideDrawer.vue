<script setup>
import {Menu, MenuButton, MenuItem, MenuItems} from '@headlessui/vue'
import {ChevronDownIcon} from '@heroicons/vue/20/solid'
import {useAuth0} from "@auth0/auth0-vue";
import {HomeIcon} from "@heroicons/vue/20/solid/index.js";
import LoginButton from "@/components/common/LoginButton.vue";
import LogoutButton from "@/components/common/LogoutButton.vue";

const {isAuthenticated, idTokenClaims} = useAuth0()
</script>

<template>
  <aside id="logo-sidebar"
         aria-label="Sidebar"
         class="fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700">
    <div class="h-full flex flex-col justify-between px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800">
      <ul class="space-y-2">
        <li>
          <router-link
              class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
              to="/">
            <HomeIcon
                class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"></HomeIcon>
            <span class="ml-3">Home</span>
          </router-link>
        </li>
        <li>
          <Menu as="div" class="relative inline-block text-left w-full">
            <div>
              <MenuButton
                  class="w-full flex justify-between items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                <div class="flex">
                  <svg aria-hidden="true"
                       class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                       fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>
                  </svg>
                  <span class="flex-1 ml-3 whitespace-nowrap">Vacancies</span>
                </div>

                <ChevronDownIcon aria-hidden="true" class="-mr-1 h-5 w-5 text-gray-400"/>
              </MenuButton>
            </div>

            <transition enter-active-class="transition ease-out duration-100"
                        enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                        leave-active-class="transition ease-in duration-75"
                        leave-from-class="transform opacity-100 scale-100"
                        leave-to-class="transform opacity-0 scale-95">
              <MenuItems
                  class="absolute right-0 z-10 mt-2 w-56 origin-top-left rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div class="py-1">
                  <MenuItem v-slot="{ active }">
                    <router-link :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                       to="/vacancies">View All</router-link>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <router-link :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                       to="/vacancies/create">Create New</router-link>
                  </MenuItem>
                </div>
              </MenuItems>
            </transition>
          </Menu>
        </li>
        <li>
          <router-link v-if="isAuthenticated"
                       class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
                       to="/">
            <svg aria-hidden="true"
                 class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                 fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path
                  d="M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z"></path>
              <path
                  d="M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"></path>
            </svg>
            <span class="flex-1 ml-3 whitespace-nowrap">My Applications</span>
            <span
                class="hidden inline-flex items-center justify-center w-3 h-3 p-3 ml-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">3</span>
          </router-link>
        </li>
      </ul>
      <ul class="space-y-2">
        <li>
          <LoginButton v-if="!isAuthenticated"
                       :class="'w-full flex items-center p-2 text-base text-left font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-blue-400 hover:text-blue-500'">
            <svg aria-hidden="true"
                 class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
                 fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path clip-rule="evenodd"
                    d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z"
                    fill-rule="evenodd"></path>
            </svg>
            <span class="flex-1 ml-3 whitespace-nowrap">Sign In</span>
          </LoginButton>
          <LogoutButton v-else
                        :class="'w-full flex items-center p-2 text-base text-left font-normal text-red-50 rounded-lg bg-red-400 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-blue-400 hover:text-blue-500'">
            <svg aria-hidden="true"
                 class="flex-shrink-0 w-6 h-6 text-white transition duration-75 dark:text-red-100 group-hover:text-gray-900 dark:group-hover:text-white"
                 fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path clip-rule="evenodd"
                    d="M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z"
                    fill-rule="evenodd"></path>
            </svg>
            <span class="flex-1 ml-3 whitespace-nowrap">Sign Out</span>
          </LogoutButton>
        </li>
      </ul>
    </div>
  </aside>
</template>