import { UserService } from './../services/user.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.css']
})
export class ProfilePageComponent implements OnInit {
  phoneChange: boolean = false;
  eMailChange: boolean = false;
  personalDataChange: boolean = false;


  constructor(private userService: UserService) { }

  ngOnInit(): void {
  }
  changePhone() {
    this.phoneChange = !this.phoneChange;
  }
  savePhone() {
    this.phoneChange = !this.phoneChange;
  }
  changeEMail() {
    this.eMailChange = !this.eMailChange;
  }
  saveEMail() {
    this.eMailChange = !this.eMailChange;
  }
  changePersonalData() {
    this.personalDataChange = !this.personalDataChange;
  }
  savePersonalData() {
    this.personalDataChange = !this.personalDataChange;
  }
}
