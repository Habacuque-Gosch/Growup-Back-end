<template>


<div class="text-center mb-3">
    <p>Sign in with:</p>

    <a data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
        <i class="bi bi-google"></i>
    </a>
    <p class="text-center">or:</p>

</div>

<form action="/index" class="form-control">

    <!-- Email input -->
    <div data-mdb-input-init class="form-outline mb-4">
        <label class="form-label" for="loginName">Email or username</label>
        <input type="email" id="loginName" class="form-control" />
    </div>

    <!-- Password input -->
    <div data-mdb-input-init class="form-outline mb-4">
        <label class="form-label" for="loginPassword">Password</label>
        <input type="password" id="loginPassword" class="form-control" />
    </div>

    <!-- 2 column grid layout -->
    <div class="row mb-4">
        <div class="col-md-6 d-flex justify-content-center">
        <!-- Checkbox -->
        <div class="form-check mb-3 mb-md-0">
            <input class="form-check-input" type="checkbox" value="" id="loginCheck" checked />
            <label class="form-check-label" for="loginCheck"> Remember me </label>
        </div>
        </div>

        <div class="col-md-6 d-flex justify-content-center">
        <!-- Simple link -->
        <a href="#!">Forgot password?</a>
        </div>
    </div>

    <!-- Submit button -->
    <button type="submit" class="btn btn-primary">Login</button>

    <!-- Register buttons -->
    <div class="text-center">
        <RouterLink :to="{name: 'register'}" class="nav-link" >Register</RouterLink>

    </div>
</form>

</template>


<script>

</script>