import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import background from '../assets/background_login.png'
import backgroundDesktop from '../assets/background_login_desktop.png'

export default class Login extends Component {
    constructor(props) {
        super(props)

        this.state = {

        }
    }

    render() {
        return (
            <section className='min-w-full container grid mx-auto bg-cover bg-center bg-fixed md:grid-cols-12' style={{ backgroundImage: `linear-gradient( rgba(10, 12, 55, 0.85), rgba(63, 63, 63, 0.55) ), url(${background})` }}>

                <div className='hidden md:grid md:items-center h-screen bg-cover bg-center w-screen' style={{ backgroundImage: `linear-gradient( rgba(10, 12, 55, 0.85), rgba(63, 63, 63, 0.55) ), url(${backgroundDesktop})` }}>
                    <div className='md:grid md:grid-cols-12'>
                        <div className='md:col-span-5 lg:col-span-6'>
                            <h1 className='text-white text-center'>Logo</h1>
                        </div>
                    </div>
                </div>

                <div className='mt-32 md:mt-0 rounded-t-[40px] md:rounded-tr-none md:w-full md:rounded-l-[50px] md:col-start-6 lg:col-start-7 md:col-span-7 lg:col-span-6 md:h-screen md:justify-self-center md:content-center bg-white px-6 md:px-10 lg:px-16 py-12 grid gap-6'>
                    <div className='text-center'>
                        <h1 className='text-secondary'>Welcome back</h1>
                        <p className='text-thirdy'>Welcome back! Please enter your details.</p>
                    </div>

                    <div>
                        <label className="label">
                            <span className="label-text text-secondary text-base">Email Address</span>
                        </label>
                        <input type="email" placeholder="user@gmail.com" className="input input-bordered input-md w-full" />
                    </div>

                    <div>
                        <label className="label">
                            <span className="label-text text-secondary text-base">Password</span>
                        </label>
                        <input type="password" placeholder="****" className="input input-bordered input-md w-full" />
                    </div>

                    <div className="flex flex-col w-full border-opacity-50">
                        <button className="btn w-full md:btn-md bg-secondary normal-case">Sign in</button>

                        <div className="divider font-signika text-thirdy">OR</div>

                        <div className="grid gap-5 place-items-center">
                            <button className="btn w-full normal-case md:btn-md">Wide</button>
                            <p className='text-thirdy'>Don’t have an account? <Link to={'./signup'} className='underline underline-offset-2 text-secondary'>Sign Up for free</Link></p>
                        </div>
                    </div>
                </div>
            </section>
        )
    }
}
