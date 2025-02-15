<template>

<div class="tab-pane fade show active" id="pills-register" role="tabpanel" aria-labelledby="tab-register">

        <form action="/user/login/" method="get">

            <!-- Name input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <input type="text" id="registerName" class="form-control" />
                <label class="form-label" for="registerName">Name</label>
            </div>

            <!-- Username input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <input type="text" id="registerUsername" class="form-control" />
                <label class="form-label" for="registerUsername">Username</label>
            </div>

            <!-- Email input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <input type="email" id="registerEmail" class="form-control" />
                <label class="form-label" for="registerEmail">Email</label>
            </div>

            <!-- Password input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <input type="password" id="registerPassword" class="form-control" />
                <label class="form-label" for="registerPassword">Password</label>
            </div>

            <!-- Repeat Password input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <input type="password" id="registerRepeatPassword" class="form-control" />
                <label class="form-label" for="registerRepeatPassword">Repeat password</label>
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
            <button class="btn btn-primary btn-block mb-3">Resgister account</button>
            
        </form>
</div>

</template>


<script>

</script>