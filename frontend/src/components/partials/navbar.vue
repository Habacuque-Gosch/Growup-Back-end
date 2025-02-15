<script>

</script>

<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-primary" data-bs-theme="dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">Growup</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <RouterLink to="/index" class="nav-link active" >Home</RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to="/course/add-course" class="nav-link">Criar curso<i class="bi bi-add"></i></RouterLink>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Profile
                    </a>
                    <ul class="dropdown-menu">
                        <RouterLink to="/user/register" class="dropdown-item"><i class="bi bi-person"></i> Profile</RouterLink>
                        <RouterLink to="/user/login" class="dropdown-item"><i class="bi bi-person-circle"></i> Login</RouterLink>
                        <RouterLink to="/user/register" class="dropdown-item"><i class="bi bi-person-circle"></i> Register</RouterLink>
                        <RouterLink to="/user/register" class="dropdown-item"><i class="bi bi-arrow-left"></i> Logout</RouterLink>
                    </ul>
                </li>
            </ul>
            </div>
        </div>
    </nav>


</template>