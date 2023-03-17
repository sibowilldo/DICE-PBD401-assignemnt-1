<script setup>
import AppLayout from '@/Layouts/AppLayout.vue'
import {getHome} from "@/services/vacancies.service.js";
import {useAuth0} from "@auth0/auth0-vue";
import {ref} from 'vue';
import Vacancy from "@/components/Vacancy.vue";

const vacancies = ref('')
const getHomeData = async () => {
  const {getAccessTokenSilently} = useAuth0()
  const accessToken = await getAccessTokenSilently()
  const {data, error} = await getHome(accessToken)

  if (data)
    vacancies.value = data.vacancies

  if (error)
    vacancies.value = error
}

getHomeData()
</script>
<template>
  <AppLayout>
    <template #page_header>
      <div>
        <h2>Home</h2>
      </div>
    </template>
    <div>
      <ul>
        <li v-for="(vacancy, index) in vacancies">
          <Vacancy :vacancy="vacancy"/>
        </li>
      </ul>
    </div>
  </AppLayout>
</template>