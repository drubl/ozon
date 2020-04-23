import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {UserService} from "../../../../services/user.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  @Output() backEmitter: EventEmitter<any> = new EventEmitter();
  @Output() onRegistrationUser: EventEmitter<any> = new EventEmitter<any>();
  public email: string;
  public password: string;
  public username: string;

  constructor(private userService: UserService) {
  }

  ngOnInit(): void {
  }

  registrationUser() {
    const userRegistrationData = {
      email: this.email,
      password: this.password,
      username: this.username
    }
    this.onRegistrationUser.emit(userRegistrationData)
  }

  goToBack() {
    this.backEmitter.emit();
  }
}
