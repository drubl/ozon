import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {UserService} from "../../../../services/user.service";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  @Output() backEmitter: EventEmitter<any> = new EventEmitter();
  public email: string;
  public password: string;
  public username: string;

  constructor(private userService: UserService) {
  }

  ngOnInit(): void {
  }
  registrationUser(){
    this.userService.registerUser({
      email: this.email,
      password: this.password,
      username: this.username
    })
  }
  goToBack() {
    this.backEmitter.emit();
  }
}
