<template>

    <p v-if="errorMessages" class="alert alert-info" role="alert">{{ errorMessages }}</p>
    <Message severity="success" variant="outlined">Success Message</Message>

</template>


<script>
import { ref } from 'vue';
export default {
    setup(){
        var errorMessages = ref('')
        errorMessages = 'erro'
        return {errorMessages}
    }
}
</script>