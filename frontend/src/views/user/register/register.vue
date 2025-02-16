<template>

<!-- <div class="tab-pane fade show active" id="pills-register" role="tabpanel" aria-labelledby="tab-register"> -->

        <form @submit.prevent="createUser" class="form-control">
            <p>{{ errorMessage }}</p>
            <!-- Name input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <label class="form-label" for="registerName">Digite seu nome completo</label>
                <input type="text" v-model="newUser.full_name" class="form-control" />
            </div>

            <!-- Username input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <label class="form-label" for="registerUsername">Username</label>
                <input type="text" v-model="newUser.username" class="form-control" />
            </div>

            <!-- Email input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <label class="form-label" for="registerEmail">Email</label>
                <input type="email" v-model="newUser.email" class="form-control" />
            </div>

            <!-- Password input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <label class="form-label" for="registerPassword">Password</label>
                <input type="password" v-model="newUser.password" class="form-control" />
            </div>

            <!-- Repeat Password input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <label class="form-label">Repeat password</label>
                <input type="password" id="registerrepeatpassword" v-model="password_repeat" class="form-control" />
            </div>

            <!-- Checkbox -->
            <div class="form-check d-flex justify-content-center mb-4">
                <input class="form-check-input me-2" type="checkbox" value="" id="registerCheck" checked
                aria-describedby="registerCheckHelpText" />
                <label class="form-check-label" for="registerCheck">
                I have read and agree to the terms
                </label>
            </div>

            <!-- Submit button -->
            <button class="btn btn-primary">Resgister account</button>
            
        </form>
<!-- </div> -->

</template>


<script>

import { ref } from 'vue';
import { baseAPI } from '@/api/axios_api'
import { useRouter } from 'vue-router';

export default {
    setup(){
        const newUser = ref({full_name: '', username: '', email: '', password: ''})
        const password_repeat = ref('')
        const errorMessage = ref('')
        const router = useRouter()

        console.log(password_repeat)

        const createUser = async()=> {
            try {
                if(newUser.value.password == password_repeat.value){

                    let config = {
                        headers: {
                            Authorization: 'Token c2ef737289fabeae006a6b01c9ecb40aa088d046',
                        }
                    }

                    const response = baseAPI.post('users/register-user/', newUser.value, config)
                    router.push({name: 'login'})

                } else {
                    errorMessage.value = `Senhas não são iguais`
                    router.push({name: 'register'})
                }
            }

            catch (error){
                console.log(`ERRO AO CRIAR USER: ${error}`)
                errorMessage.value = `Erro ao registrar-se`
            }
        }

        return {
            newUser,
            createUser,
            password_repeat,
            errorMessage
        }
    }
}


</script>