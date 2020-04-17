import { Component, OnInit } from '@angular/core';
import {Auth} from "../../../auth";
import {Router} from "@angular/router";

export class CustomerLogin {
  email: string;
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
      email: this.login,
      password: this.password
    };
    this.auth.login(loginCustomer).subscribe(answer => {
      console.log(answer);
    });
  }
}
