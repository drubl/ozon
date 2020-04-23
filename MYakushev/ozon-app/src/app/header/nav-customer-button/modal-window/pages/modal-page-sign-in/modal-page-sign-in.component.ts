import {Component, EventEmitter, Output} from '@angular/core';
import {AuthLoginData} from '../../../../../core/auth/auth.service';


@Component({
  selector: 'app-modal-page-sign-in',
  templateUrl: './modal-page-sign-in.component.html',
  styleUrls: ['./modal-page-sign-in.component.css']
})


export class ModalPageSignInComponent {
  @Output() logInUserData: EventEmitter<AuthLoginData> = new EventEmitter<AuthLoginData>();
  @Output() onPageSignInClickReg: EventEmitter<string> = new EventEmitter<string>();
  login = '';
  password = '';

  submitLogIn() {
    const userLogInData: AuthLoginData = {
      username: this.login,
      password: this.password
    };
    this.logInUserData.emit(userLogInData);
  }
  clickRegistration() {
    this.onPageSignInClickReg.emit();
  }
}
