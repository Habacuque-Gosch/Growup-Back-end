<template>

    <p v-if="errorFlash" class="alert alert-info" role="alert">{{ errorFlash }}</p>

</template>


<script>
import { ref } from 'vue';
export default {
    setup(){
        var errorFlash = ref('')
        // errorMessages = 'erro'
        return {errorFlash}
    }
}
</script>