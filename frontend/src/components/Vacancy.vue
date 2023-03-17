<script setup>
import moment from "moment";
import {ArchiveBoxIcon, CalendarDaysIcon, ClockIcon, FolderIcon, MapPinIcon} from "@heroicons/vue/24/outline/index.js";
import {useAuth0} from "@auth0/auth0-vue";

const {isAuthenticated} = useAuth0()
const props = defineProps(['vacancy'])

</script>
<template>
  <div
      class="dark:bg-gray-800 bg-gray-50 border-dashed border-gray-200 dark:border-gray-700 border-2 p-5 rounded-2xl space-y-2 mb-10">
    <div class="space-y-3">
      <h2>
        <router-link class="dark:text-white text-gray-800 text-2xl decoration decoration-1 hover:decoration-dotted"
                     to="#">
          {{ props.vacancy.title }}
        </router-link>
      </h2>
      <ul class="flex gap-3">
        <li v-if="props.vacancy.user" class="border-gray-300 bg-blue-100 text-gray-800 py-1 px-2 text-xs rounded">Posted
          By:
          {{ props.vacancy.user.profile.composed_name }}
        </li>
        <li class="border-gray-300 bg-red-100 text-gray-800 py-1 px-2 text-xs rounded">{{
            props.vacancy.department
          }}
        </li>
      </ul>
    </div>
    <div>
      <ul class="flex gap-5">
        <li class="text-sm flex items-center gap-1 font-bold text-xs">
          <FolderIcon class="h-4 w-4"/>
          Job Category
        </li>
        <li class="text-sm flex items-center gap-1 font-bold text-xs">
          <ArchiveBoxIcon class="h-4 w-4"/>
          Type
        </li>
        <li class="text-sm flex items-center gap-1 font-bold text-xs">
          <MapPinIcon class="h-4 w-4"/>
          {{ props.vacancy.location }}
        </li>
      </ul>
    </div>
    <div v-if="props.vacancy.description" class="text-xs text-gray-600 dark:text-gray-400"
         v-html="props.vacancy.description.substring(1,10) !== '' ? props.vacancy.description : 'No Description'">
    </div>
    <div class="flex justify-between items-center">
      <ul class="flex font-mono text-xs gap-5">
        <li v-if="props.vacancy.created_at" class="flex gap-1">
          <ClockIcon class="h-4 w-4"/>
          {{ moment(props.vacancy.created_at).fromNow() }}
        </li>
        <li v-if="props.vacancy.expires_at" class="expires flex gap-1">
          <CalendarDaysIcon class="h-4 w-4"/>
          <span :title="moment(props.vacancy.expires_at)">
                    {{ moment(props.vacancy.expires_at) < moment() ? 'Expired ' : 'Expires ' }} {{
              moment(props.vacancy.expires_at).fromNow()
            }}
                  </span>
        </li>
      </ul>
      <div class="flex gap-5">
        <button v-if="isAuthenticated" class="text-blue-50 px-4 py-2 bg-blue-500 text-white rounded text-xs uppercase shadow-blue shadow-md hover:shadow"
                type="button">
          <i class="far fa-star"></i>
          Apply
        </button>
        <a class="show-more btnLoaderTrigger px-4 py-2 rounded text-xs uppercase bg-gray-100">Show
          More</a>
      </div>
    </div>
  </div>
</template>