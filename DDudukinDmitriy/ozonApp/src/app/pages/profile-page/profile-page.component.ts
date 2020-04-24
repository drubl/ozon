import {UserService} from '../../services/user.service';
import {Component, OnInit} from '@angular/core';
import {UserData} from "../../../User";

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.css']
})
export class ProfilePageComponent implements OnInit {
  public profileData: UserData;
  public phoneChange: boolean = false;
  public eMailChange: boolean = false;
  public personalDataChange: boolean = false;
  public email: string;
  public phone: string;
  public name: string;
  public gender: string;
  public birthday: string;


  constructor(private userService: UserService) {
  }

  ngOnInit(): void {
    this.getUserData();
  }

  changePhone() {
    this.phoneChange = !this.phoneChange;
  }

  savePhone() {
    this.phoneChange = !this.phoneChange;
    this.userService.savePhone({
      phone: this.phone
    }).subscribe()
  }

  changeEMail() {
    this.eMailChange = !this.eMailChange;
  }

  saveEMail() {
    this.eMailChange = !this.eMailChange;
    this.userService.saveEmail({
      email: this.email
    }).subscribe()
  }

  changePersonalData() {
    this.personalDataChange = !this.personalDataChange;
  }

  savePersonalData() {
    this.personalDataChange = !this.personalDataChange;
    this.userService.savePersonalData({
      name: this.name,
      birthday: this.birthday,
      gender: this.gender
    }).subscribe()
  }

  public getUserData() {
    this.userService.getCustomerData()
      .subscribe(data => {
        this.profileData = data;
      })
  }

  public exit() {
    this.userService.exit().subscribe(data => {
        window.location.reload()
      }
    )
  }

  public deleteUser() {
    this.userService.deleteUser().subscribe(data => {
      window.location.reload()
    })
  }
}
