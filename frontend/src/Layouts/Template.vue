<script setup>
const getTheme = () => {
  if (window.localStorage.getItem('dark')) {
    return JSON.parse(window.localStorage.getItem('dark'))
  }
  return !!window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
}

const setTheme = (value) => {
  window.localStorage.setItem('dark', value)
}

let loading = true
const isDark = getTheme()
const toggleTheme = () => {
  this.isDark = !isDark
  setTheme(isDark)
}
const setLightTheme = () => {
  this.isDark = false
  setTheme(isDark)
}
const setDarkTheme = () => {
  this.isDark = true
  setTheme(isDark)
}
const watchScreen = () => {
  if (window.innerWidth <= 1024) {
    this.isSidebarOpen = false
  } else if (window.innerWidth >= 1024) {
    this.isSidebarOpen = true
  }
}
let isSidebarOpen = window.innerWidth >= 1024
const toggleSidbarMenu = () => {
  this.isSidebarOpen = !isSidebarOpen
}
let isNotificationsPanelOpen = false
const
openNotificationsPanel = () => {
  this.isNotificationsPanelOpen = true
  this.$nextTick(() => {
    this.$refs.notificationsPanel.focus()
  })
}
let isSettingsPanelOpen = false
const
openSettingsPanel = () => {
  this.isSettingsPanelOpen = true
  this.$nextTick(() => {
    this.$refs.settingsPanel.focus()
  })
}
let isSearchPanelOpen = false
const
openSearchPanel = () => {
  this.isSearchPanelOpen = true
  this.$nextTick(() => {
    this.$refs.searchInput.focus()
  })
}


const init = () => {
  return {}
}

init();
</script>
<template>
  <div
      :class="{ 'dark': isDark }"
      x-data="setup()"
      x-init="$refs.loading.classList.add('hidden');"
      @resize.window="watchScreen()"
  >
    <div class="flex h-screen antialiased text-gray-900 bg-gray-100 dark:bg-dark dark:text-light">
      <!-- Loading screen -->
      <div
          class="fixed inset-0 z-50 flex items-center justify-center text-2xl font-semibold text-white bg-indigo-800"
          x-ref="loading"
      >
        Loading.....
      </div>

      <!-- Sidebar -->
      <!-- Backdrop -->
      <div
          aria-hidden="true"
          class="fixed inset-0 z-10 bg-indigo-800 lg:hidden"
          style="opacity: 0.5"
          x-show="isSidebarOpen"
          @click="isSidebarOpen = false"
      ></div>

      <aside
          class="fixed inset-y-0 z-10 flex flex-shrink-0 overflow-hidden bg-white border-r lg:static dark:border-indigo-800 dark:bg-darker focus:outline-none"
          tabindex="-1"
          x-ref="sidebar"
          x-show="isSidebarOpen"
          x-transition:enter="transition-all transform duration-300 ease-in-out"
          x-transition:enter-end="translate-x-0 opacity-100"
          x-transition:enter-start="-translate-x-full opacity-0"
          x-transition:leave="transition-all transform duration-300 ease-in-out"
          x-transition:leave-end="-translate-x-full opacity-0"
          x-transition:leave-start="translate-x-0 opacity-100"
          @keydown.escape="window.innerWidth <= 1024 ? isSidebarOpen = false : ''"
      >
        <!-- Mini column -->
        <div class="flex flex-col flex-shrink-0 h-full px-2 py-4 border-r dark:border-indigo-800">
          <!-- Brand -->
          <div class="flex-shrink-0">
            <a
                class="inline-block text-xl font-bold tracking-wider text-indigo-700 uppercase dark:text-light"
                href="#"
            >
              K-WD
            </a>
          </div>

          <!-- Mini column footer -->
          <div class="relative flex items-center justify-center flex-shrink-0">
            <!-- User avatar button -->
            <div class="" x-data="{ open: false }">
              <button
                  :aria-expanded="open ? 'true' : 'false'"
                  aria-haspopup="true"
                  class="block transition-opacity duration-200 rounded-full dark:opacity-75 dark:hover:opacity-100 focus:outline-none focus:ring dark:focus:opacity-100"
                  type="button"
                  @click="open = !open; $nextTick(() => { if(open){ $refs.userMenu.focus() } })"
              >
                <span class="sr-only">User menu</span>
                <img
                    alt="Ahmed Kamel"
                    class="w-10 h-10 rounded-full"
                    src="https://avatars.githubusercontent.com/u/57622665?s=460&u=8f581f4c4acd4c18c33a87b3e6476112325e8b38&v=4"
                />
              </button>

              <!-- User dropdown menu -->
              <div
                  aria-label="User menu"
                  aria-orientation="vertical"
                  class="absolute w-56 py-1 mb-4 bg-white rounded-md shadow-lg min-w-max left-5 bottom-full ring-1 ring-black ring-opacity-5 dark:bg-dark focus:outline-none"
                  role="menu"
                  tabindex="-1"
                  x-ref="userMenu"
                  x-show="open"
                  x-transition:enter="transition-all transform ease-out"
                  x-transition:enter-end="translate-y-0 opacity-100"
                  x-transition:enter-start="-translate-y-1/2 opacity-0"
                  x-transition:leave="transition-all transform ease-in"
                  x-transition:leave-end="-translate-y-1/2 opacity-0"
                  x-transition:leave-start="translate-y-0 opacity-100"
                  @click.away="open = false"
                  @keydown.escape="open = false"
              >
                <a
                    class="block px-4 py-2 text-sm text-gray-700 transition-colors hover:bg-gray-100 dark:text-light dark:hover:bg-indigo-600"
                    href="#"
                    role="menuitem"
                >
                  Your Profile
                </a>
                <a
                    class="block px-4 py-2 text-sm text-gray-700 transition-colors hover:bg-gray-100 dark:text-light dark:hover:bg-indigo-600"
                    href="#"
                    role="menuitem"
                >
                  Settings
                </a>
                <a
                    class="block px-4 py-2 text-sm text-gray-700 transition-colors hover:bg-gray-100 dark:text-light dark:hover:bg-indigo-600"
                    href="#"
                    role="menuitem"
                >
                  Logout
                </a>
              </div>
            </div>
          </div>
        </div>
        <!-- Sidebar links -->
        <nav aria-label="Main" class="flex-1 w-64 px-2 py-4 space-y-2 overflow-y-hidden hover:overflow-y-auto">
          <!-- Dashboards links -->
          <div x-data="{ isActive: false, open: false}">
            <!-- active & hover classes 'bg-indigo-100 dark:bg-indigo-600' -->
            <a
                :aria-expanded="(open || isActive) ? 'true' : 'false'"
                :class="{'bg-indigo-100 dark:bg-indigo-600': isActive || open}"
                aria-haspopup="true"
                class="flex items-center p-2 text-gray-500 transition-colors rounded-md dark:text-light hover:bg-indigo-100 dark:hover:bg-indigo-600"
                href="#"
                role="button"
                @click="$event.preventDefault(); open = !open"
            >
                <span aria-hidden="true">
                  <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                        d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                    />
                  </svg>
                </span>
              <span class="ml-2 text-sm"> Dashboards </span>
              <span aria-hidden="true" class="ml-auto">
                  <!-- active class 'rotate-180' -->
                  <svg
                      :class="{ 'rotate-180': open }"
                      class="w-4 h-4 transition-transform transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
                  </svg>
                </span>
            </a>
            <div aria-label="Dashboards" class="mt-2 space-y-2 px-7" role="menu" x-show="open">
              <!-- active & hover classes 'text-gray-700 dark:text-light' -->
              <!-- inActive classes 'text-gray-400 dark:text-gray-400' -->
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:text-gray-400 dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Default
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Project Mangement
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                E-Commerce
              </a>
            </div>
          </div>

          <!-- Components links -->
          <div x-data="{ isActive: false, open: false }">
            <!-- active classes 'bg-indigo-100 dark:bg-indigo-600' -->
            <a
                :aria-expanded="(open || isActive) ? 'true' : 'false'"
                :class="{ 'bg-indigo-100 dark:bg-indigo-600': isActive || open }"
                aria-haspopup="true"
                class="flex items-center p-2 text-gray-500 transition-colors rounded-md dark:text-light hover:bg-indigo-100 dark:hover:bg-indigo-600"
                href="#"
                role="button"
                @click="$event.preventDefault(); open = !open"
            >
                <span aria-hidden="true">
                  <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                        d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                    />
                  </svg>
                </span>
              <span class="ml-2 text-sm"> Components </span>
              <span aria-hidden="true" class="ml-auto">
                  <!-- active class 'rotate-180' -->
                  <svg
                      :class="{ 'rotate-180': open }"
                      class="w-4 h-4 transition-transform transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
                  </svg>
                </span>
            </a>
            <div arial-label="Components" class="mt-2 space-y-2 px-7" role="menu" x-show="open">
              <!-- active & hover classes 'text-gray-700 dark:text-light' -->
              <!-- inActive classes 'text-gray-400 dark:text-gray-400' -->
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:text-gray-400 dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Alerts
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:text-gray-400 dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Buttons
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Cards
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Dropdowns
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Forms
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Lists
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Modals
              </a>
            </div>
          </div>

          <!-- Pages links -->
          <div x-data="{ isActive: false, open: false }">
            <!-- active classes 'bg-indigo-100 dark:bg-indigo-600' -->
            <a
                :aria-expanded="(open || isActive) ? 'true' : 'false'"
                :class="{ 'bg-indigo-100 dark:bg-indigo-600': isActive || open }"
                aria-haspopup="true"
                class="flex items-center p-2 text-gray-500 transition-colors rounded-md dark:text-light hover:bg-indigo-100 dark:hover:bg-indigo-600"
                href="#"
                role="button"
                @click="$event.preventDefault(); open = !open"
            >
                <span aria-hidden="true">
                  <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                        d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                    />
                  </svg>
                </span>
              <span class="ml-2 text-sm"> Pages </span>
              <span aria-hidden="true" class="ml-auto">
                  <!-- active class 'rotate-180' -->
                  <svg
                      :class="{ 'rotate-180': open }"
                      class="w-4 h-4 transition-transform transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
                  </svg>
                </span>
            </a>
            <div arial-label="Pages" class="mt-2 space-y-2 px-7" role="menu" x-show="open">
              <!-- active & hover classes 'text-gray-700 dark:text-light' -->
              <!-- inActive classes 'text-gray-400 dark:text-gray-400' -->
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:text-gray-400 dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Blank
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:text-gray-400 dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Profile
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Pricing
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Kanban
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Feed
              </a>
            </div>
          </div>

          <!-- Authentication links -->
          <div x-data="{ isActive: false, open: false}">
            <!-- active & hover classes 'bg-indigo-100 dark:bg-indigo-600' -->
            <a
                :aria-expanded="(open || isActive) ? 'true' : 'false'"
                :class="{'bg-indigo-100 dark:bg-indigo-600': isActive || open}"
                aria-haspopup="true"
                class="flex items-center p-2 text-gray-500 transition-colors rounded-md dark:text-light hover:bg-indigo-100 dark:hover:bg-indigo-600"
                href="#"
                role="button"
                @click="$event.preventDefault(); open = !open"
            >
                <span aria-hidden="true">
                  <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                    />
                  </svg>
                </span>
              <span class="ml-2 text-sm"> Authentication </span>
              <span aria-hidden="true" class="ml-auto">
                  <!-- active class 'rotate-180' -->
                  <svg
                      :class="{ 'rotate-180': open }"
                      class="w-4 h-4 transition-transform transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
                  </svg>
                </span>
            </a>
            <div aria-label="Authentication" class="mt-2 space-y-2 px-7" role="menu" x-show="open">
              <!-- active & hover classes 'text-gray-700 dark:text-light' -->
              <!-- inActive classes 'text-gray-400 dark:text-gray-400' -->
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Register
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Login
              </a>
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Password Reset
              </a>
            </div>
          </div>

          <!-- Layouts links -->
          <div x-data="{ isActive: true, open: true}">
            <!-- active & hover classes 'bg-indigo-100 dark:bg-indigo-600' -->
            <a
                :aria-expanded="(open || isActive) ? 'true' : 'false'"
                :class="{'bg-indigo-100 dark:bg-indigo-600': isActive || open}"
                aria-haspopup="true"
                class="flex items-center p-2 text-gray-500 transition-colors rounded-md dark:text-light hover:bg-indigo-100 dark:hover:bg-indigo-600"
                href="#"
                role="button"
                @click="$event.preventDefault(); open = !open"
            >
                <span aria-hidden="true">
                  <svg
                      class="w-5 h-5"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                    />
                  </svg>
                </span>
              <span class="ml-2 text-sm"> Layouts </span>
              <span aria-hidden="true" class="ml-auto">
                  <!-- active class 'rotate-180' -->
                  <svg
                      :class="{ 'rotate-180': open }"
                      class="w-4 h-4 transition-transform transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
                  </svg>
                </span>
            </a>
            <div aria-label="Authentication" class="mt-2 space-y-2 px-7" role="menu" x-show="open">
              <!-- active & hover classes 'text-gray-700 dark:text-light' -->
              <!-- inActive classes 'text-gray-400 dark:text-gray-400' -->
              <a
                  class="block p-2 text-sm text-gray-400 transition-colors duration-200 rounded-md dark:text-gray-400 dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Two Columns Sidebar
              </a>
              <a
                  class="block p-2 text-sm text-gray-700 transition-colors duration-200 rounded-md dark:text-light dark:hover:text-light hover:text-gray-700"
                  href="#"
                  role="menuitem"
              >
                Mini + One Columns Sidebar
              </a>
            </div>
          </div>
        </nav>
      </aside>

      <!-- Sidebars button -->
      <div class="fixed flex items-center space-x-4 top-5 right-10 lg:hidden">
        <button
            class="p-1 text-indigo-400 transition-colors duration-200 rounded-md bg-indigo-50 hover:text-indigo-600 hover:bg-indigo-100 dark:hover:text-light dark:hover:bg-indigo-700 dark:bg-dark focus:outline-none focus:ring"
            @click="isSidebarOpen = true; $nextTick(() => { $refs.sidebar.focus() })"
        >
          <span class="sr-only">Toggle main manu</span>
          <span aria-hidden="true">
              <svg
                  class="w-8 h-8"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  x-show="!isSidebarOpen"
                  xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M4 6h16M4 12h16M4 18h16" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
              </svg>
              <svg
                  class="w-8 h-8"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  x-show="isSidebarOpen"
                  xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M6 18L18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
              </svg>
            </span>
        </button>
      </div>

      <!-- Main content -->
      <main class="flex-1">
        <div
            class="flex flex-col items-center justify-center flex-1 h-full min-h-screen p-4 overflow-x-hidden overflow-y-auto">
          <slot/>
        </div>
      </main>

    </div>

  </div>

</template>