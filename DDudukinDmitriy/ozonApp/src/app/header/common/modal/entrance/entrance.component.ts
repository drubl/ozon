import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {UserService} from "../../../../services/user.service";

@Component({
    selector: 'app-entrance',
    templateUrl: './entrance.component.html',
    styleUrls: ['./entrance.component.css']
})
export class EntranceComponent implements OnInit {
    @Output() onRegistrationFromEntrance: EventEmitter<any> = new EventEmitter<any>();
    @Output() onEntrance: EventEmitter<any> = new EventEmitter<any>();

    username: string = '';
    password: string = '';

    constructor(private userService: UserService) {
    }

    ngOnInit(): void {
    }

    entranceEmitter() {
        const loginPassword = {
            username: this.username,
            password: this.password
        }
        this.onEntrance.emit(loginPassword);
    }

    public register(): void {
        this.onRegistrationFromEntrance.emit()
    }
}

