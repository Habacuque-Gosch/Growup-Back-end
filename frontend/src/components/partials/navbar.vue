<script setup>


</script>


<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">Growup</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <!-- <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li> -->

                    <!-- <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="">Categorias</a>
                    </li> -->

                    <!-- <a href="" class="btn btn-danger">Logout <i class="bi bi-person-circle"></i></a> -->

                    <div class="">
                        <RouterLink to="/course/add-course" class="btn btn-success mt-2">Criar curso<i class="bi bi-add"></i></RouterLink>
                    </div>

                    <div class="">
                        <RouterLink to="/user/login" class="btn btn-success mt-2">Login <i class="bi bi-person-circle"></i></RouterLink>
                        <RouterLink to="/user/register" class="btn btn-primary mt-2">Register <i class="bi bi-person-circle"></i></RouterLink>
                    </div>

                </ul>
            </div>
        </div>
    </nav>


</template>