<template>
    <div class="bg-ctid-navy text-white">
        <div class="xl:max-w-[1536px] mx-auto p-16 xl:py-20 lg:px-32 2xl:px-16 xl:flex">
            <div class=" xl:w-1/2 xl:pr-10">
                <h1>
                    <router-link to="/">
                        <h1>MITRE Fight Fraud Framework</h1>
                    </router-link>
                </h1>
                <p class="my-4">
                    The <a href="https://ctid.mitre.org/?utm_source=fight-financial-fraud" target="_blank"
                        class="underline hover:text-ctid-light-blue">Center for Threat-Informed Defense</a> is a
                    non-profit, privately funded research and development organization. Our
                    mission is to advance the state of the art and the state of the practice in threat-informed defense
                    globally.
                </p>
                <div class="md:flex">
                    <img src="../assets/ctid-logo-horizontal-white.png" class="h-6 my-auto"
                        alt="Center for Threat Informed Defense" />
                    <div class="social-links">
                        <a href="mailto:ctid@mitre.org?subject=Fight%20Financial%20Fraud"
                            aria-label="center for threat-informed defense email" class="email">
                            <i class="pi pi-envelope"></i>
                        </a>
                        <a href="https://www.linkedin.com/showcase/center-for-threat-informed-defense/" target="blank"
                            aria-label="center for threat-informed defense on linkedin" class="linkedin">
                            <i class="pi pi-linkedin"></i>
                        </a>
                        <a href="https://www.youtube.com/playlist?list=PLALq3Th79NnpUkRy8TUYVBKvysCp9xwNh"
                            target="blank" class="youtube" aria-label="center for threat-informed defense youtube">
                            <i class="pi pi-youtube"></i>
                        </a>
                        <a href="https://github.com/center-for-threat-informed-defense/" target="blank" class="github"
                            aria-label="center for threat-informed defense github">
                            <i class="pi pi-github"></i>
                        </a>
                    </div>
                </div>
            </div>
            <div class="xl:max-w-1/2 xl:pl-10 xl:my-auto mt-8">
                <div class="flex w-full  content-between">
                    <div class="w-1/2">
                        <h2 class="mt-8">About</h2>
                        <ul>
                            <li><router-link to="/about/methodology">Design Principles</router-link></li>
                            <li><router-link to="/about/contributors">Contributors</router-link></li>
                            <li><router-link to="/about/contact-us">Contact Us</router-link></li>
                        </ul>
                    </div>
                    <div class="w-1/2">
                        <h2 class="mt-8">Resources</h2>
                        <ul>
                            <li><router-link to="/matrix">Matrix</router-link></li>
                            <li><router-link to="/tactic">Tactics</router-link></li>
                            <li><router-link to="/technique">Techniques</router-link></li>
                        </ul>
                    </div>
                </div>
                <p class="my-4 public-release">© 2026 MITRE. Approved for public release. Document number(s)
                    PR_25-02691-6.</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    data() {
        return {
            externalProjects: [
                { label: "Attack Flow", route: "https://center-for-threat-informed-defense.github.io/attack-flow/" },
                { label: "M3TID", route: "https://center-for-threat-informed-defense.github.io/m3tid/" },
                { label: "Mappings Explorer", route: "https://center-for-threat-informed-defense.github.io/mappings-explorer/" },
                { label: "Summiting the Pyramid", route: "https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/" },
            ]
        };
    },
});
</script>

<style scoped>
h1 {
    @apply text-3xl font-medium
}

h2 {
    @apply text-xl font-semibold mt-0
}

.public-release {
    @apply text-sm mb-0
}

.social-links {
    @apply flex md:ml-8 md:my-0 my-4 gap-6 xl:gap-4 2xl:gap-8
}

.social-links a {
    @apply bg-ctid-light-blue hover:bg-white text-ctid-navy rounded-full flex h-8 w-8 my-auto text-center;
}

.social-links i {
    @apply m-auto;

}

ul {
    @apply list-inside;
    list-style-type: square;
}

li a {
    @apply hover:underline hover:text-ctid-light-blue
}
</style>