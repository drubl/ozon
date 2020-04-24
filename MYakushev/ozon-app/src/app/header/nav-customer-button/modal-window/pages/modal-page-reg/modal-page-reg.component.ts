import {Component, EventEmitter, OnInit, Output} from '@angular/core';

export class AuthRegData {
  username: string;
  email: string;
  password: string;
}

@Component({
  selector: 'app-modal-page-reg',
  templateUrl: './modal-page-reg.component.html',
  styleUrls: ['./modal-page-reg.component.css']
})
export class ModalPageRegComponent {
  @Output() regDataOutput: EventEmitter<AuthRegData> = new EventEmitter<AuthRegData>();
  @Output() onPageRegClickBack: EventEmitter<string> = new EventEmitter<string>();

  regLogin = '';
  regMail = '';
  regPassword = '';


  regEmit() {
    const userDataRegistration = {
      username: this.regLogin,
      email: this.regMail,
      password: this.regPassword,
    };
    this.regDataOutput.emit(userDataRegistration);
  }
  regBackEmit() {
    this.onPageRegClickBack.emit();
  }
}
