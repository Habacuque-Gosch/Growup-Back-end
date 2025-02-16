<template>

    <p v-if="errorMessages" class="alert alert-info" role="alert">{{ errorMessages }}</p>

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