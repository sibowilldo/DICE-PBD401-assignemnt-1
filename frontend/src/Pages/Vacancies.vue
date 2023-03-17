<script setup>
import AppLayout from '@/Layouts/AppLayout.vue'
import {getVacancies} from "@/services/vacancies.service.js";
import {useAuth0} from "@auth0/auth0-vue";
import {ref} from 'vue';
import Vacancy from "@/components/Vacancy.vue";

const vacancies = ref('')
const getVacanciesData = async () => {
  const {getAccessTokenSilently} = useAuth0()
  const accessToken = await getAccessTokenSilently()
  const {data, error} = await getVacancies(accessToken)

  if (data)
    vacancies.value = data.vacancies

  if (error)
    vacancies.value = error
}

getVacanciesData()
</script>
<template>
  <AppLayout>
    <template #page_header>
      <h2>Vacancies</h2>
    </template>
    <div>
      <ul class="space-5">
        <li v-for="vacancy in vacancies" :key="vacancy.id">
          <Vacancy :vacancy="vacancy"/>
        </li>
      </ul>
    </div>
  </AppLayout>
</template>