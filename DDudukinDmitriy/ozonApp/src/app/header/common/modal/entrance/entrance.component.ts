import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {UserService} from "../../../../services/user.service";

@Component({
  selector: 'app-entrance',
  templateUrl: './entrance.component.html',
  styleUrls: ['./entrance.component.css']
})
export class EntranceComponent implements OnInit {
  @Output() registerEmitter: EventEmitter<any> = new EventEmitter<any>();
  username: string = '';
  password: string = '';

  constructor(private userService: UserService) {
  }

  ngOnInit(): void {
  }

  public entrance() {
    this.userService.getUserId({
      username: this.username,
      password: this.password
    }).subscribe(id => {
      window.location.reload()
    })
  }

  public register(): void {
    this.registerEmitter.emit()
  }
}
