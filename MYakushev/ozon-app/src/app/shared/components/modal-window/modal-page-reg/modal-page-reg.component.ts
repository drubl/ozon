import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {UserRegistration} from '../../../interfaces';

@Component({
  selector: 'app-modal-page-reg',
  templateUrl: './modal-page-reg.component.html',
  styleUrls: ['./modal-page-reg.component.scss']
})
export class ModalPageRegComponent implements OnInit {
  @Output() showModalLoginHandler: EventEmitter<any> = new EventEmitter<any>();
formReg: FormGroup;
  constructor() { }

  ngOnInit() {
    this.formReg = new FormGroup({
      login: new FormControl(null, [
          Validators.required,
          Validators.minLength(4),
      ]),
      email: new FormControl(null, [
        Validators.required,
          Validators.email,
      ]),
      password: new FormControl(null, [
        Validators.required,
        Validators.minLength(6),
      ])
    });
  }

  submitReg() {
    if (this.formReg.invalid) {
      return;
    }
    const userRegistration: UserRegistration = {
      login: this.formReg.value.login,
      email: this.formReg.value.email,
      password: this.formReg.value.password
    };
    console.log(userRegistration);
  }

  showModalLogin() {
    this.showModalLoginHandler.emit();
    this.formReg.reset();
  }
}
