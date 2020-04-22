import { Component, OnInit } from '@angular/core';
import {Auth} from "../../../auth";
import {Router} from "@angular/router";

export class CustomerLogin {
  username: string;
  password: string | number;
}

@Component({
  selector: 'app-modal-reg',
  templateUrl: './modal-reg.component.html',
  styleUrls: ['./modal-reg.component.css']
})
export class ModalRegComponent implements OnInit {
  toggleLeftSignIn = true;
  toggleLeftReg = true;
  toggleLeft = true;
  login = '';
  password = '';

  regLogin = '';
  regPassword = '';
  regMail = '';

  regStatus: string;

  constructor(private auth: Auth, private router: Router) { }
  authId: number;
  ngOnInit(): void {
  }

  choiseLeftSignIn() {
    this.toggleLeftSignIn = !this.toggleLeftSignIn;
    this.toggleLeft = !this.toggleLeft;
  }

  choiseLeftReg() {
    this.toggleLeftReg = !this.toggleLeftReg;
    this.toggleLeft = !this.toggleLeft;
  }

  choiseBack() {
    this.toggleLeftSignIn = true;
    this.toggleLeftReg = true;
    this.toggleLeft = true;
  }

  signIn($event: Event) {
    $event.preventDefault();
    if (!this.login.trim() || !this.password.trim()) {
      return console.log('Пустая строка');
    }
    const loginCustomer = {
      username: this.login,
      password: this.password
    };
    this.auth.login(loginCustomer).subscribe(answer => {
      console.log(answer);
      this.router.navigate(['/cart']);
      window.location.reload();
    });
  }
  registration($event: Event) {
    $event.preventDefault();
    if (!this.regLogin.trim() || !this.regPassword.trim() || !this.regMail.trim()) {
      return console.log('Пустая строка');
    }
    const registrationCustomer = {
      username: this.regLogin,
      password: this.regPassword,
      email: this.regMail
    };
    this.auth.registration(registrationCustomer).subscribe(answer => {
      if (answer) {
        this.regStatus = 'Регистрация прошла успешно';
        setTimeout(() => {
          this.toggleLeftSignIn = false;
          this.toggleLeftReg = true;
          this.toggleLeft = false;
        }, 1200);
      }
    });
  }
}
