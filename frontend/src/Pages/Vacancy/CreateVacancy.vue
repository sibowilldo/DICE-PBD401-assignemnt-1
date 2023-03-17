<script setup>
import AppLayout from "@/Layouts/AppLayout.vue";
import TextInput from "@/components/forms/TextInput.vue";

/**
 * user_id
 * category_id
 * type_id
 * title
 * description
 * department
 * location
 * expires_at
 */
const form = {
  expires_at: '',
  type: ''
}

const saveVacancy = () => console.log('Saving... '+ form.type, form )

</script>

<template>
  <AppLayout>
    <div class="mt-10 sm:mt-0">
      <div class="md:grid md:grid-cols-3 md:gap-6">
        <div class="md:col-span-1">
          <div class="px-4 sm:px-0">
            <h3 class="text-xl font-semibold leading-6 text-gray-800 dark:text-gray-100">Vacancy Information</h3>
            <p class="mt-1 text-sm text-gray-300">Use a permanent address where you can receive mail.</p>
          </div>
        </div>
        <div class="mt-5 md:col-span-2 md:mt-0">
          <form action="#" method="POST">
            <div class="overflow-hidden shadow sm:rounded-md">
              <div class="bg-white px-4 py-5 sm:p-6 dark:bg-opacity-5 dark:bg-blue-500">
                <div class="grid grid-cols-6 gap-6">
                  <div class="col-span-12 sm:col-span-12">
                    <label class="block text-sm font-bold leading-6 text-gray-900 dark:text-white" for="first-name">Title</label>
                    <input id="first-name" class="mt-2 block w-full
                    rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 dark:bg-gray-700
                    dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                    placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600
                    sm:text-sm sm:leading-6" name="first-name" placeholder="eg: Assistant Lecture (4 Posts)"
                           type="text"/>
                  </div>
                  <div class="col-span-12 sm:col-span-12">
                    <label class="block text-sm font-bold leading-6 text-gray-900 dark:text-white" for="last-name">Description</label>
                    <textarea id="about"
                              class="mt-1 block w-full rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset
                              dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                              ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset
                              focus:ring-indigo-600 sm:py-1.5 sm:text-sm sm:leading-6"
                              name="about"
                              rows="3"/>
                  </div>


                  <div class="col-span-6 sm:col-span-12 lg:col-span-6">
                    <label class="block text-sm font-bold leading-6 text-gray-900 dark:text-white"
                           for="street-address">Department</label>
                    <input id="street-address"
                           class="mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1
                           dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                           ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset
                           focus:ring-indigo-600 sm:text-sm sm:leading-6"
                           placeholder="Information Technology"
                           type="text"/>
                  </div>

                  <div class="col-span-6 sm:col-span-12 lg:col-span-6">
                    <label class="block text-sm font-bold leading-6 text-gray-900 dark:text-white"
                           for="city">Location</label>
                    <select id="location"
                            class="mt-2 block w-full rounded-md border-0 bg-white py-1.5 text-gray-900 shadow-sm
                            dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                            ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600
                            sm:text-sm sm:leading-6"
                            name="location">
                      <option>Steve Biko Campus-Durban</option>
                      <option>Ritson Campus-Durban</option>
                      <option>Ml Sultan Campus-Durban</option>
                      <option>Indumiso Campus-PMB</option>
                    </select>
                  </div>

                  <div class="lg:col-span-4 md:col-span-4 col-span-12">
                    <label class="block text-sm font-bold leading-6 text-gray-900 dark:text-white" for="country">Category</label>
                    <select id="country"
                            class="mt-2 block w-full rounded-md border-0 bg-white py-1.5 text-gray-900 shadow-sm
                            dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                            ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600
                            sm:text-sm sm:leading-6"
                            name="country">
                      <option>United States</option>
                      <option>Canada</option>
                      <option>Mexico</option>
                    </select>
                  </div>
                  <div class="lg:col-span-4 md:col-span-4 col-span-12">
                    <label class="block text-sm font-bold leading-6 text-gray-900 dark:text-white"
                           for="country">Type</label>
                    <select id="type"
                            class="mt-2 block w-full rounded-md border-0 bg-white py-1.5 text-gray-900 shadow-sm ring-1
                            dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                            ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm
                            sm:leading-6"
                            v-model="form.type">
                      <option>United States</option>
                      <option>Canada</option>
                      <option>Mexico</option>
                    </select>
                  </div>
                  <div class="lg:col-span-4 md:col-span-4 col-span-12">
                    <label class="bloboldt-sm font-bold leading-6 text-gray-900 dark:text-white" for="country">Expires
                      at</label>
                    <TextInput
                        id="expires_at"
                        class="mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1
                                dark:bg-gray-700 dark:ring-gray-600 dark: ring-2 dark:text-gray-200
                                ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset
                                focus:ring-indigo-600 sm:text-sm sm:leading-6"
                        v-model="form.expires_at"
                        type="date"/>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 text-right sm:px-6 dark:bg-gray-800">
                <button
                    class="inline-flex justify-center rounded-md bg-indigo-600 py-2 px-3 text-sm font-semibold
                    text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2
                    focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
                    type="submit" @click.prevent="saveVacancy">
                  Save
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </AppLayout>
</template>
