<template>
<aside :class="`${is_expanded && 'is-expanded'}`">
    <div class="logo">
        <img src="../assets/logo.png" alt="CPSS">
    </div>

    <div class="menu-toggle-wrap">
        <button class="menu-toggle" @click="ToggleMenu">
            <span class="span material-icons">keyboard_double_arrow_right</span>
        </button>
    </div>
	<h3>Menu</h3>
		<div class="menu">
			<router-link to="/" class="button">
				<span class="material-icons">dashboard</span>
				<span class="text">Services</span>
			</router-link>
			<router-link to="/rules" class="button">
				<span class="material-icons">density_medium</span>
				<span class="text">Rules</span>
			</router-link>
			<router-link to="/about" class="button">
				<span class="material-icons">info</span>
				<span class="text">About</span>
			</router-link>
		</div>
  </aside>
</template>

<script setup>
import { ref } from 'vue'
import logoURL from '../assets/logo.png'

const is_expanded = ref(localStorage.getItem("is_expanded") === "true")

const ToggleMenu = () => {
	is_expanded.value = !is_expanded.value
	localStorage.setItem("is_expanded", is_expanded.value)
}
</script>


<style lang="scss" scoped>
aside {
	display: flex;
	flex-direction: column;

	background-color: var(--dark);
	color: var(--light);

	width: calc(2rem + 32px);
	overflow: hidden;
	min-height: 100vh;
	padding: 1rem;

	transition: 0.2s ease-in-out;

	.flex {
		flex: 1 1 0%;
	}

	.logo {
		margin-bottom: 1rem;

		img {
			width: 2rem;
		}
	}
    .menu-toggle-wrap {
		display: flex;
		justify-content: flex-end;
        margin-bottom: 1rem;

        position: relative;
		top: 0;
		transition: 0.2s ease-in-out;
        .menu-toggle {
			transition: 0.2s ease-in-out;
			.material-icons {
				font-size: 2rem;
				color: var(--light);
				transition: 0.2s ease-out;
			}
            &:hover {
                .material-icons {
                    color: var(--primary);
                    transform: translateX(0.5rem);
				    transition: 0.2s ease-out;
                    
                }
            }
        }
    }


	h3, .button .text {
		opacity: 0;
		transition: opacity 0.3s ease-in-out;
	}

	h3 {
		color: var(--grey);
		font-size: 0.875rem;
		margin-bottom: 0.5rem;
		text-transform: uppercase;
	}
	.menu {
		margin: 0 -1rem;

		.button {
			display: flex;
			align-items: center;
			text-decoration: none;

			padding: 0.5rem 1rem;
			transition: 0.2s ease-in-out;


			.material-icons {
				font-size: 2rem;
				color: var(--light);
				transition: 0.2s ease-in-out;
			}
			.text {
				color: var(--light);
				transition: 0.2s ease-in-out;
			}

			&:hover, &.router-link-active {
				background-color: var(--dark-alt);

				.material-icons, .text {
					color: var(--primary);
				}
			}

			&.router-link-active {
				background-color: var(--dark-alt);
				border-right: 5px solid var(--primary);

				.material-icons, .text {
					color: var(--primary);
				}
			}
		}
	}

	.footer {
		opacity: 0;
		transition: opacity 0.3s ease-in-out;

		p {
			font-size: 0.875rem;
			color: var(--grey);
		}
	}


	&.is-expanded {
		width: var(--sidebar-width);
        .logo{
            img {
                width: 6rem;
            }
        }
		.menu-toggle-wrap {
			top: -6rem;
            .menu-toggle {
                transform: rotate(-180deg);
            }
        }
		h3, .button .text {
			opacity: 1;
		}
		
		.button {
			.material-icons {
				margin-right: 1rem;
			}
		}

		.footer {
			opacity: 0;
		}
    }
	@media (max-width: 1024px) {
		position: absolute;
		z-index: 99;
	}
}
</style>